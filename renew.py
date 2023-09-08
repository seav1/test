import requests


def postpone_hibernation(api_token):
    url = "https://aperture.section.io/api/v1/accounts/me/sites/all/hibernation"
    headers = {"Authorization": "Bearer {}".format(api_token)}
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    api_token = open("sectionio_api_token.txt", "r").read()
    success = postpone_hibernation(api_token)
    print("Postpone hibernation succeeded" if success else "Postpone hibernation failed")
