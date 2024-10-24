function initializeBonusCalculator() {
    var einzahlungsbetrags = document.querySelectorAll(".einzahlungsbetrag");
    var gesamtguthabens = document.querySelectorAll(".gesamtguthaben");
    var bonusguthabens = document.querySelectorAll(".bonusguthaben");
    var wagers = document.querySelectorAll(".wager");

    einzahlungsbetrags.forEach(function (einzahlungsbetragInput, index) {
        einzahlungsbetragInput.addEventListener("input", function () {
            var einzahlungsbetrag = parseFloat(einzahlungsbetragInput.value);
            var bonusValue = parseFloat(einzahlungsbetragInput.getAttribute("data-casino-bonus"));
            var bonusMax = parseFloat(einzahlungsbetragInput.getAttribute("data-casino-bonus-max"));
            var bonusWager = parseFloat(einzahlungsbetragInput.getAttribute("data-casino-bonus-wager"));

            var bonusguthaben = einzahlungsbetrag * (bonusValue / 100);

            // Limit bonusguthaben to bonus_max
            if (bonusguthaben >= bonusMax) {
                bonusguthaben = bonusMax;
            }

            var gesamtguthaben = einzahlungsbetrag + bonusguthaben;
            var wager = gesamtguthaben * bonusWager;

            gesamtguthabens[index].textContent = "Guthaben: " + gesamtguthaben.toFixed(0) + "€";
            bonusguthabens[index].textContent = "Bonus: " + bonusguthaben.toFixed(0) + "€";
            wagers[index].textContent = "Wager: " + wager.toFixed(0) + "€";
        });
    });
}

document.addEventListener("DOMContentLoaded", initializeBonusCalculator);

// Call initializeBonusCalculator after sorting the casino list
initializeBonusCalculator();
