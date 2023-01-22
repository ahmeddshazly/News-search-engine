<template>
  <div class="container">
    <form @submit.prevent="search" class="search-bar">
      <input
        v-model="query"
        placeholder="Search for news"
        type="text"
        required
      />
      <select class="language" v-model="selectedLang">
        <option disabled value="">Language</option>
        <option v-for="option in options" :key="option" :value="option.value">
          {{ option.text }}
        </option>
      </select>
      <button><font-awesome-icon icon="search" /></button>
    </form>

    <div class="articles">
      <article v-for="article in paginatedArticles" :key="article">
        <header>
          <vue-load-image>
            <template v-slot:image>
              <img :src="article.urlToImage" />
            </template>
            <template v-slot:preloader>
              <font-awesome-icon icon="spinner" />
            </template>
            <template v-slot:error
              ><font-awesome-icon icon="image" size="6x"
            /></template>
          </vue-load-image>
        </header>
        <section>
          <a :href="article.url" target="_blank">{{ article.title }}</a>
          <p>
            {{ article.description }}
          </p>
        </section>
      </article>
      <div v-if="hasArticles" class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">
          Previous
        </button>
        <button
          @click="nextPage"
          :disabled="
            currentPage === Math.ceil(articles.length / articlesPerPage)
          "
        >
          Next
        </button>
      </div>
    </div>
    <div v-if="searched && articles.length === 0" class="no-results">
      <h3>No results found</h3>
      <p>Please try again with the following suggestions:</p>
      <ul>
        <li>Check your spelling</li>
        <li>Use more specific keywords</li>
        <li>Try different keywords</li>
        <li>Expand your search by using broader terms</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import VueLoadImage from "vue-load-image";
export default {
  components: {
    "vue-load-image": VueLoadImage,
  },
  data() {
    return {
      query: "",
      articles: [],
      searched: false,
      selectedLang: "",
      options: [
        { text: "English", value: "en" },
        { text: "Deutsch", value: "de" },
      ],
      currentPage: 1,
      articlesPerPage: 20,
    };
  },
  computed: {
    //checking articles availability
    hasArticles() {
      return this.articles.length > 0;
    },
    //distributing articles to pages
    paginatedArticles() {
      const start = (this.currentPage - 1) * this.articlesPerPage;
      const end = start + this.articlesPerPage;
      return this.articles.slice(start, end);
    },
  },
  methods: {
    prevPage() {
      this.currentPage =
        this.currentPage > 1 ? this.currentPage - 1 : this.currentPage;
    },
    nextPage() {
      this.currentPage =
        this.currentPage <
        Math.ceil(this.articles.length / this.articlesPerPage)
          ? this.currentPage + 1
          : this.currentPage;
    },
    async search() {
      var params = new URLSearchParams();
      params.append("query", this.query);
      params.append("language", this.selectedLang);
      var request = {
        params: params,
      };
      try {
        const path = "http://127.0.0.1:5000";
        let response = await axios.get(path + `/search`, request);
        this.articles = response.data.articles;
        this.currentPage = 1;
      } catch (error) {
        console.log(error);
      }
      this.searched = true;
    },
  },
};
</script>
<style>
.container {
  width: 100%;
  min-height: 100vh;
  padding: 5px 0px;
  background-color: lightgray;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.search-bar {
  width: 100%;
  min-height: 20px;
  max-width: 700px;
  background: rgba(255, 255, 255, 0.2);
  align-items: center;
  display: flex;
  border-radius: 60px;
  padding: 10px 20px;
  backdrop-filter: blur(4px) saturate(180%);
}
.search-bar input {
  background: transparent;
  flex: 1;
  border: 0;
  outline: none;
  padding: 24px 20px;
  font-size: 20px;
}
.search-bar button {
  border: 0;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  background: transparent;
  cursor: pointer;
}
@media screen and (max-width: 600px) {
  .search-bar {
    flex-wrap: wrap;
    justify-content: center;
    width: 80% !important;
  }
  .search-bar input {
    width: 100%;
    margin-bottom: 10px;
    font-size: 14px;
    padding: 5px;
  }
  .search-bar button {
    margin-left: 10px;
    font-size: 14px;
    padding: 5px;
  }
}

.articles {
  padding-top: 30px;
  display: flex;
  flex-direction: column;
}
.articles article {
  display: grid;
  grid-column-start: 1;
  grid-column-end: end;
  grid-template-columns: 200px auto 40px;
  grid-template-rows: 100px;
  border-bottom: 10px solid #ccc;
  overflow: hidden;
  cursor: pointer;
}
.articles header {
  display: flex;
  justify-content: center;
  align-items: center;
}
.articles header img {
  max-width: 100%;
  height: auto;
  border-radius: 15%;
}
.articles section {
  padding: 5px 25px;
  max-height: 100px;
  overflow: hidden;
  text-align: left;
}
.articles section p {
  text-overflow: ellipsis;
  white-space: nowrap;
}
.language {
  background-color: #ccc;
  width: 20%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

.language:focus {
  outline: none;
}

.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
}

.pagination button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.pagination button:hover {
  background-color: #3e8e41;
}

.pagination button[disabled] {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination button[disabled]:hover {
  background-color: #ccc;
}
.no-results {
  background-color: #3e424b;
  color: #fff;
  padding: 20px;
  text-align: left;
  border-radius: 10px;
  margin: 20px 0;
  box-shadow: 2px 2px 10px #8b5e3c;
  width: 50%;
  margin: 0 auto;
}
.no-results h3 {
  font-size: 2rem;
  margin-bottom: 20px;
}
.no-results ul {
  margin-top: 20px;
  list-style: inside;
  text-align: left;
}
.no-results li {
  font-size: 1.2rem;
  margin-bottom: 10px;
}
</style>
