$cupcakesUl = $("#cupcakes");
$cupcakeForm = $("#cupcake-form");

async function getAllCupcakes() {
    let resp;
    try {
        resp = await axios.get("/api/cupcakes");
    } catch (e) {
        console.error(e);
    }
    return resp.data.cupcakes;
}

async function updateCupcakesList() {
    const cupcakes = await getAllCupcakes();
    for (const cupcake of cupcakes) {
        addCupcakeListItem(cupcake);
    }
}

function addCupcakeListItem(cupcake) {
    const $li = $("<li>").html(`
        <p>${cupcake.size} ${cupcake.flavor}</p>
        <p><b>Rating:</b>${cupcake.rating}</p>
        <img src="${cupcake.image}" />
    `).data("id", cupcake.id);
    $cupcakesUl.append($li);
}

updateCupcakesList();

async function addCupcake(details) {
    let resp;
    try {
        resp = await axios.post("/api/cupcakes", data=details);
    } catch (e) {
        console.error(e);
    }
    addCupcakeListItem(resp.data.cupcake);
}

$cupcakeForm.on("submit", e => {
    e.preventDefault();
    flavor = $cupcakeForm.find("#flavor").val();
    rating = +$cupcakeForm.find("#rating").val();
    size = $cupcakeForm.find("#size").val();
    image = $cupcakeForm.find("#image").val();
    details = {flavor, rating, size};
    if (image) details.image = image;
    addCupcake(details);
    $cupcakeForm[0].reset()
});
