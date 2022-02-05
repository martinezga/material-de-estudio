
const API_URL = 'https://some-random-api.ml/animal/'
const API_ENDPOINTS = [
    'dog',
    'cat',
    'panda',
    'fox',
    'red_panda',
    'koala',
    'birb',
    'racoon',
    'kangaroo',
]

const getRandomEndpoint = () => {
    const randomIndex = Math.floor(Math.random() * API_ENDPOINTS.length)
    return API_ENDPOINTS[randomIndex]
};

const searchAnimal = async () => {
    const randomEndpoint = getRandomEndpoint();
    const url = `${API_URL}${randomEndpoint}`;
    const answer = await fetch(url);
    const data = await answer.json();
    return data
};

const showAnimal = (data) => {
    const image_received = data.image;
    const animal_fact = data.fact;
    const container = document.querySelector('.random-pic');
    const img = document.createElement("img");
    const fact = document.createElement("figcaption");

    container.appendChild(img);
    container.appendChild(fact);

    img.setAttribute("src", image_received);
    img.setAttribute("alt", "animal");
    img.classList.add("py-3");
    fact.innerHTML = animal_fact;
};

const animal = searchAnimal();

animal.then(data => {
    showAnimal(data);
});
