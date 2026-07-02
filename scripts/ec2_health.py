import boto3
import csv
import os

ec2_client = boto3.client("ec2")
response = ec2_client.describe_instances()

# Map state names to emoji-decorated labels
STATE_ICONS = {
    "running": "🟢 Running",
    "stopped": "🔴 Stopped",
    "pending": "🟡 Pending",
    "stopping": "🟠 Stopping",
    "shutting-down": "🟠 Shutting Down",
    "terminated": "⚫ Terminated",
}


def get_instance_name(instance):
    """Pull the 'Name' tag if it exists, else return 'N/A'."""
    for tag in instance.get("Tags", []):
        if tag["Key"] == "Name":
            return tag["Value"]
    return "N/A"


def get_state_label(state_name):
    """Return an emoji-decorated state label for console output."""
    return STATE_ICONS.get(state_name, state_name.capitalize())


# --- Resolve paths relative to THIS script's location, not the cwd ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

REPORT_PATH = os.path.join(REPORTS_DIR, "ec2_report.csv")

# --- Print header ---
print("=" * 36)
print("AWS EC2 HEALTH REPORT")
print("=" * 36)
print()

# --- Write CSV + print console report in a single pass ---
with open(REPORT_PATH, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Instance ID", "State", "Instance Type", "Public IP"])

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            name = get_instance_name(instance)
            instance_id = instance["InstanceId"]
            state_name = instance["State"]["Name"]
            instance_type = instance["InstanceType"]
            public_ip = instance.get("PublicIpAddress", "N/A")
            state_label = get_state_label(state_name)

            # Console output (pretty, with emoji)
            print(f"Instance ID   : {instance_id}")
            print(f"State         : {state_label}")
            print(f"Type          : {instance_type}")
            print(f"Public IP     : {public_ip}")
            print(f"Name          : {name}")
            print()
            print("-" * 36)

            # CSV output (plain, machine-readable — raw state, no emoji)
            writer.writerow([name, instance_id, state_name, instance_type, public_ip])

print(f"\nReport written to {REPORT_PATH}")
print("Connected to AWS SDK")