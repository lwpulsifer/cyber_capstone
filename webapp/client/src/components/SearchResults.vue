<template>
  <b-container>
    <h1>Voter Data</h1>
    <b-table striped hover :items='voter_data'></b-table>
  <div>
    <b-button v-on:click='getMessage'>Render</b-button>
  </div>
  <br><br>
  <div class="hello">
    <router-link to="/" tag='b-button'>Back to search</router-link>
  </div>
  </b-container>
</template>

<script>
import axios from 'axios';
// import router from '../router';

export default {
  name: 'SearchResults',
  data() {
    return {
      voter_data: ['Stuff', 'Things'],
    };
  },
  watch: {
    $route() {
      this.getMessage();
    },
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/results';
      axios.get(path)
        .then((res) => {
          this.voter_data = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    mounted() {
      this.getMessage();
    },
    updated() {
      this.getMessage();
    },
  },
};
</script>
