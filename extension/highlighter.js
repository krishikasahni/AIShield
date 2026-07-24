function highlightSpam(element, confidence) {

    element.style.backgroundColor = "#ffebee";
    element.style.border = "2px solid red";
    element.style.borderRadius = "8px";
    element.style.padding = "4px";

    const badge = document.createElement("span");

    badge.innerText = ` ⚠️ Spam (${Math.round(confidence * 100)}%)`;

    badge.style.color = "red";
    badge.style.fontWeight = "bold";
    badge.style.marginLeft = "8px";

    element.appendChild(badge);
}