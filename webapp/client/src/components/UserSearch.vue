<template>
  <b-container>
  <b-container v-if="show_search">
    <div>
      <h1> Find out what data of yours are floating around on the internet
      </h1>
    </div><br>
    <div class="container">
      <!-- <b-button v-b-modal.searchmodal> Search </b-button> -->
        <b-form @submit="onSubmit" class="w-100">
        <b-input-group prepend="Name"
                      id="form-title-group"
                      label="Name"
                      label-for="form-name-input">
            <b-form-input id="form-first-name-input"
                          type="text"
                          v-model="searchForm.first_name"
                          placeholder="Enter first name (Optional)">
            </b-form-input>
            <b-form-input id="form-middle-name-input"
                            type="text"
                            v-model="searchForm.middle_initial"
                            placeholder="MI">
            </b-form-input>
            <b-form-input id="form-last-name-input"
                            type="text"
                            v-model="searchForm.last_name"
                            required
                            placeholder="Enter last name">
            </b-form-input>
        </b-input-group>
        <b-input-group prepend="Twitter Handle">
          <b-form-input id="form-handle-input"
                              type="text"
                              v-model="searchForm.handle"
                              placeholder="Enter twitter handle (optional)">
          </b-form-input>
        </b-input-group>
        <br>
          <b-button type="submit" variant="primary">Go</b-button>
        </b-form>
      </div>
  </b-container>
  <b-container v-if="!show_search">
      <h1>Voter Data</h1>
      <b-table striped hover :items='voter_data'></b-table>
    <br>
    <div class="back-to-search">
      <b-button v-on:click="toggleSearch"> Return to Search </b-button>
    </div>
  </b-container>
  </b-container>
</template>

<script>
import axios from 'axios';

const NProgress = require('nprogress');

export default {
  name: 'UserSearch',
  data() {
    return {
      msg: 'Stuff!',
      searchForm: {
        first_name: '',
        last_name: '',
        middle_initial: '',
        handle: '',
      },
      show_search: true,
      voter_data: [],
    };
  },
  methods: {
    initForm() {
      this.searchForm.first_name = '';
      this.searchForm.last_name = '';
      this.searchForm.middle_initial = '';
      this.handle = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        first_name: this.searchForm.first_name,
        last_name: this.searchForm.last_name,
        middle_initial: this.searchForm.middle_initial,
        handle: this.handle,
      };
      this.sendSearch(payload);
    },
    sendSearch(payload) {
      const path = 'http://localhost:5000/search';
      NProgress.start();
      axios.post(path, payload)
        .then((response) => {
          // eslint-disable-next-line
          console.log(response.data.search_result);
          NProgress.done();
          this.show_search = false;
          this.getMessage();
          // this.$router.push({ name: 'SearchResults' });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
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
    toggleSearch() {
      this.show_search = true;
      console.log(this.show_search);
    },
  },
  // created() {
  //   this.getMessage();
  // },
};
</script>
