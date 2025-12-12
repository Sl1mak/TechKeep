document.getElementById("login_form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch("/loginUser", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (data.message === "Login successful") {
        window.location.href = "/";
    } else {
        alert("Invalid credentials");
    }
})
