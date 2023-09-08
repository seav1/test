import os
import requests

API_ENDPOINT = "url = "https://aperture.section.io/api/v1/accounts/me/sites/all/hibernation"

# 指定需要进行续期操作的节点 ID 和天数
NODE_ID = 43009
DAYS_TO_POSTPONE = 7

def renew_hibernation(api_key, node_id, days):
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"days": days, "node_id": node_id}
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    if response.ok:
        print(f"Hibernation postponed for {days} days on node ID {node_id}")
    else:
        print(f"Failed to postpone hibernation on node ID {node_id}")

if __name__ == '__main__':
    api_key = os.environ.get("SECTION_IO_API_KEY")
    renew_hibernation(api_key, NODE_ID, DAYS_TO_POSTPONE)
