document.getElementById("register_form").addEventListener("submit", async (e) => {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const password_confirm = document.getElementById("password_confirm").value;

    const response = await fetch("/registerUser", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify({ username, password, email})
    });

    const data = await response.json();

    if (data.message === "Login successful" && password === password_confirm) {
        window.location.href = "/";
    } else {
        alert("Invalid credentials");
    }
})
