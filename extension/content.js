console.log("AIShield Started");

const scanned = new Set();

async function scanComments() {

    const spans = document.querySelectorAll("span");

    for (const span of spans) {

        const text = span.innerText.trim();

        if (text.length < 5)
            continue;

        if (scanned.has(text))
            continue;

        scanned.add(text);

        console.log("Scanning:", text);

        const result = await predictComment(text);

        console.log(result);

        if (result && result.prediction === "Spam") {

            span.style.background = "#ff4d4f";
            span.style.color = "white";
            span.style.padding = "3px 6px";
            span.style.borderRadius = "6px";

            span.insertAdjacentHTML(
                "afterend",
                `<span style="
                    color:red;
                    font-weight:bold;
                    margin-left:6px;
                ">⚠ AIShield Spam (${Math.round(result.confidence * 100)}%)</span>`
            );
        }
    }
}

scanComments();

setInterval(scanComments, 3000);