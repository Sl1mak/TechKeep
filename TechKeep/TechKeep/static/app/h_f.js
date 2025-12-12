const logoutBtn = document.getElementById("logout");

if (logoutBtn) {
    logoutBtn.addEventListener("click", async () => {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const response = await fetch("/logoutUser", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
                "Content-Type": "application/json"
            },
            credentials: "include"
        });

        const data = await response.json();

        if (data.message === "Logout successful") {
            window.location.reload();
        }
    });
}
