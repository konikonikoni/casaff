const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const casinoList = document.querySelector('.casino_list');
let casinoItems = Array.from(casinoList.querySelectorAll('.casino_list_item'));

// Add a change event listener to the checkboxes to update the filtered list of casinos
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateCasinoList);
});

// Get the button container
const buttonContainer = document.getElementById('sort_criteria');

// Add a click event listener to the button container
buttonContainer.addEventListener('click', (event) => {
    if (event.target.tagName === 'BUTTON') {
        const criteria = event.target.getAttribute('data-criteria'); // Get the selected sorting criteria

        // Sort the items by the selected criteria
        casinoItems.sort((a, b) => {
            const elementA = a.querySelector(criteria);
            const elementB = b.querySelector(criteria);

            if (criteria === '.sort_casino_name') {
                // Sort by casino name
                const textA = elementA.textContent.trim().toLowerCase();
                const textB = elementB.textContent.trim().toLowerCase();
                return textA.localeCompare(textB);
            } else if (criteria === '.sort_casino_created') {
                // Sort by creation date (new to old)
                const dateA = new Date(elementA.textContent.trim());
                const dateB = new Date(elementB.textContent.trim());
                return dateB - dateA;
            } else if (criteria === '.sort_casino_bonus') {
                // Sort by bonus (highest first)
                const bonusA = parseInt(elementA.textContent);
                const bonusB = parseInt(elementB.textContent);
                return bonusB - bonusA;
            } else if (criteria === '.sort_casino_bonus_max') {
                // Sort by max bonus (highest first)
                const maxBonusA = parseInt(elementA.textContent);
                const maxBonusB = parseInt(elementB.textContent);
                return maxBonusB - maxBonusA;
            } else if (criteria === '.sort_casino_bonus_wager') {
                // Sort by bonus wager (lowest first)
                const wagerA = parseInt(elementA.textContent);
                const wagerB = parseInt(elementB.textContent);
                return wagerA - wagerB;
            } else {
                return 0; // Elements without the specified class are considered equal
            }
        });

        // Call updateCasinoList to filter the sorted items
        updateCasinoList();
    }
});

function updateCasinoList() {
    // Clear the casinoList
    casinoList.innerHTML = '';

    // Create an array to store selected checkbox values
    const selectedValues = [];

    // Iterate through checkboxes and add checked values to selectedValues
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            selectedValues.push(checkbox.value.toLowerCase());
        }
    });

    // Filter and display casinos in casinoList based on selectedValues
    casinoItems.forEach(item => {
        const filterCasino = item.querySelector('.filter_casino');

        initializeBonusCalculator();

        if (filterCasino) {
            const filterText = filterCasino.textContent.toLowerCase();

            // Check if all selectedValues are present in filterText
            if (selectedValues.length === 0 || selectedValues.every(value => filterText.includes(value))) {
                casinoList.appendChild(item.cloneNode(true));
            }
        }
    });
}

// Call updateCasinoList initially to set the initial state
updateCasinoList();