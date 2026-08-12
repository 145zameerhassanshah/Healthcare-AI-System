import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    """Retrieve users from the API."""

    response = requests.get(
        f"{BASE_URL}/users",
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def get_user_summary(user_id):
    """Retrieve and extract selected user information."""

    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )

    response.raise_for_status()

    user = response.json()

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"]
    }

def get_posts_by_user(user_id):
    """Retrieve posts belonging to a specific user."""

    params = {
        "userId": user_id
    }

    response = requests.get(
        f"{BASE_URL}/posts",
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def get_user(user_id):
    """Retrieve one user by ID."""

    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def create_user(name, username, email):
    """Create a new user."""

    payload = {
        "name": name,
        "username": username,
        "email": email
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def replace_user(user_id, name, username, email):
    """Replace an existing user."""

    payload = {
        "name": name,
        "username": username,
        "email": email
    }

    response = requests.put(
        f"{BASE_URL}/users/{user_id}",
        json=payload,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def update_user_email(user_id, email):
    """Partially update a user's email."""

    payload = {
        "email": email
    }

    response = requests.patch(
        f"{BASE_URL}/users/{user_id}",
        json=payload,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def delete_user(user_id):
    """Delete a user."""

    response = requests.delete(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )

    response.raise_for_status()

    return response.status_code


if __name__ == "__main__":

    print("\n--- GET: All Users ---")

    users = get_users()

    print(f"Total users received: {len(users)}")
    print(f"First user: {users[0]['name']}")
    print(f"Email: {users[0]['email']}")


    print("\n--- GET: Single User ---")

    user = get_user(1)

    print(f"ID: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")


    print("\n--- POST: Create User ---")

    new_user = create_user(
        "Healthcare AI Patient",
        "healthcare_patient",
        "patient@example.com"
    )

    print(new_user)


    print("\n--- PUT: Replace User ---")

    replaced_user = replace_user(
        1,
        "Updated Patient",
        "updated_patient",
        "updated@example.com"
    )

    print(replaced_user)


    print("\n--- PATCH: Partial Update ---")

    updated_user = update_user_email(
        1,
        "newemail@example.com"
    )

    print(updated_user)

print("\n--- GET: Posts By User ---")

posts = get_posts_by_user(1)

print(f"Posts received: {len(posts)}")

for post in posts[:3]:
    print(f"Post ID: {post['id']}")
    print(f"Title: {post['title']}")
    print("-" * 40)

    print("\n--- GET: Selected User Information ---")

    summary = get_user_summary(1)

    print(f"ID: {summary['id']}")
    print(f"Name: {summary['name']}")
    print(f"Email: {summary['email']}")
    print(f"City: {summary['city']})")

    print("\n--- DELETE: Delete User ---")

    delete_status = delete_user(1)

    print(f"Delete status code: {delete_status}")

    