chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    if (request.type === "predict") {

        fetch("http://localhost:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: request.text
            })
        })
        .then(response => response.json())
        .then(data => sendResponse(data))
        .catch(error => {
            console.error("Background Fetch Error:", error);
            sendResponse(null);
        });

        return true; // Keep the message channel open
    }

});