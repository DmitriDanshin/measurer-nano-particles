<template>
  <div class="options">
    <h1>Параметры</h1>
    <div class="options__menu">
      <div>
        <label for="showSize">Показать размер:</label>
        <input type="checkbox" id="showSize" />
      </div>
      <div>
        <label for="showBorder">Показать границу:</label>
        <input type="checkbox" id="showBorder" />
      </div>
      <div>
        <label for="showСontours">Показать контуры:</label>
        <input type="checkbox" id="showСontours" />
      </div>
      <div>
        <label for="particlesSizeNm">Размер частицы(нм):</label>
        <input type="input" id="particlesSizeNm" placeholder="200" />
      </div>
      <div>
        <label for="gaussianAccuracy">Точность фильтра Гаусса:</label>
        <input type="input" id="gaussianAccuracy" placeholder="9" />
      </div>
      <div>
        <label for="lowerThreshold">Нижняя граница оператора Кэнни:</label>
        <input type="input" id="lowerThreshold" placeholder="50" />
      </div>
      <div>
        <label for="upperThreshold">Верхняя граница оператора Кэнни:</label>
        <input type="input" id="upperThreshold" placeholder="100" />
      </div>
      <div>
        <label for="sizeAccuracy">Точность размеров:</label>
        <input type="input" id="sizeAccuracy" placeholder="19" />
      </div>
      <div>
        <label for="OperatorCanny">Оператор Кэнни:</label>
        <input type="checkbox" id="OperatorCanny" placeholder="19" />
      </div>
    </div>
  </div>
  <div class="advertising"></div>
</template>

<script>
export default {
  name: "AppOptions",
};
</script>

<style lang="scss">
.options {
  grid-column: 1;
  grid-row: 1 / 3;
  width: 450px;
  border: 1px solid rgb(2, 2, 2);
  &__menu {
    display: grid;
    justify-content: center;
    gap: 25px;
    label {
      font-size: 15px;
      font-family: "Heebo", sans-serif;
      font-style: normal;
      line-height: 10px;
      align-items: center;
      text-align: center;
      justify-content: center;
    }
    input {
      border-radius: 12px;
      margin-left: 10px;
      align-items: center;
      text-align: center;
      border: 2px solid rgb(36, 35, 35);
    }
    input:checked {
      border: 2px solid red;
    }
  }
  h1 {
    font-size: 26px;
    grid-row: 1;
    font-family: "Heebo", sans-serif;
    font-style: normal;
    font-weight: bold;
    line-height: 60px;
    margin: 10px;
    text-align: center;
  }
}
.advertising {
  width: 450px;
  display: flex;
  font-size: 26px;
  grid-row: 3;
  justify-content: center;
  border: 1px solid green;
  align-items: center;
  background-image: url('../assets/brawl.jpg');
  background-size: cover;
  
}
</style>
