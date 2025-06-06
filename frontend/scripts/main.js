
function addition() {
    const a = document.getElementById("value_a").value;
    const b = document.getElementById("value_b").value;
    const result = parseInt(a) + parseInt(b);
    document.getElementById('output').innerText = result;
}