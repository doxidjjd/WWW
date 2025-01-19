if (isNaN(meters) || meters <= 0) {
                resultDiv.textContent = "Будь ласка, введіть коректне значення!";
                return;
            }

            let result;
            switch (conversion) {
                case 1:
                    result = meters / 1609.34;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} миль;
                    break;
                case 2:
                    result = meters * 39.3701;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} дюймів;
                    break;
                case 3:
                    result = meters * 1.09361;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} ярдів;
                    break;
                case 4:
                    result = meters / 1000;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} кілометрів;
                    break;
                case 5:
                    result = meters * 100;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} сантиметрів;
                    break;
                case 6:
                    result = meters * 1000;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} міліметрів;
                    break;
                case 7:
                    result = meters * 1000000;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} мікрометрів;
                    break;
                case 8:
                    result = meters * 1e9;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} нанометрів;
                    break;
                case 9:
                    result = meters * 1e12;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} пікометрів;
                    break;
                case 10:
                    result = meters * 1e15;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} фемтометрів;
                    break;
                case 11:
                    result = meters / 1852;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} морських миль;
                    break;
                case 12:
                    result = meters * 1.057e-16;
                    resultDiv.textContent = ${meters} метрів = ${result.toExponential(6)} світових років;
                    break;
                case 13:
                    result = meters * 6.68459e-12;
                    resultDiv.textContent = ${meters} метрів = ${result.toExponential(6)} астрономічних одиниць;
                    break;
                case 14:
                    result = meters / 0.762;
                    resultDiv.textContent = ${meters} метрів = ${result.toFixed(6)} кроків людини;
                    break;
                default:
                    resultDiv.textContent = "Неправильний вибір!";
            }
        }
    </script>
</body>
</html>