<template>
  <div class="title-container">
    <h1 class="title">Daily Feed</h1>
    <NewsArticles />
  </div>
</template>

<script>
import NewsArticles from "./components/NewsArticles.vue";

export default {
  name: "app",
  components: {
    NewsArticles,
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.title-container {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.title {
  color: blue;
  font-size: 2rem;
  margin-bottom: 1rem;
  text-align: center;
  flex-basis: 100%;
}
</style>
