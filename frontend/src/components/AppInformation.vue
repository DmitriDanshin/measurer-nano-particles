<template>
  <div class="information">
    <div class="information__title">Информация</div>
    <ul class="information__list">
      <li>Количество частиц: <strong>1231</strong></li>
      <li>Максимальный размер: <strong>32</strong></li>
      <li>Минимальный размер: <strong>12</strong></li>
      <li>Средний размер: <strong>22</strong></li>
      <li>Медианный размер: <strong>15</strong></li>
      <li>Наиболее встречающийся размер: <strong>23</strong></li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "AppInformation",
};
</script>

<style lang="scss" scoped>
.information {
  grid-column: 3;
  grid-row: 1 / 3;
  background-color: #f5f5dc;
  border: 5px solid rgb(0, 0, 0);
  border-left: 0px;
  &__list {
    display: grid;
    
    margin: 10px 20px 10px 20px;
    color: rgb(0, 0, 0);
    list-style-type: none;
    gap: 30px;
    font-size: 16px;
    font-family: "Heebo", sans-serif;
    font-style: normal;
    line-height: 10px;
 
    
  }
  &__title {
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
</style>
