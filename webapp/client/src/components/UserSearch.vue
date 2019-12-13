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
          <b-button variant="primary"> # Tweets: {{ searchForm.tweet_num }}</b-button>
          <b-form-input id="form-handle-input"
                              type="range"
                              v-model="searchForm.tweet_num"
                              min="0"
                              max="100">
          </b-form-input>
        </b-input-group>
        <br>
          <b-button type="submit" variant="primary">Go</b-button>
        </b-form>
      </div>
  </b-container>
  <b-container v-if="!show_search">
    <b-row>
      <b-col>
        <h1>Voter Data for</h1>
        <h2 color='red'>{{ first_name }} {{ last_name }}</h2>
      </b-col>
      <b-col>
        <h1> Twitter Activity </h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
      <b-table class='tables'
          sticky-header='400px'
          bordered striped hover
          :items='voter_data'></b-table>
      </b-col>
    <br>
    <b-col>
      <!-- <b-card v-for="tweet in tweets" :key="tweet">
        {{ tweet }}
      </b-card> -->
      <b-table class='tables'
          sticky-header='400px'
          bordered striped hover
          :items='tweets'></b-table>
    </b-col>
    </b-row>
    <div class="back-to-search">
      <b-button v-on:click="toggleSearch"> Return to Search </b-button>
    </div>
  </b-container>
  </b-container>
</template>

<script>
import axios from 'axios';
// import { Tweet } from 'vue-tweet-embed';

const NProgress = require('nprogress');

export default {
  name: 'UserSearch',
  // components: {
  //   Tweet,
  // },
  data() {
    return {
      msg: 'Stuff!',
      searchForm: {
        first_name: '',
        last_name: '',
        middle_initial: '',
        handle: '',
        tweet_num: '50',
      },
      first_name: '',
      last_name: '',
      show_search: true,
      voter_data: [],
      tweets: [],
    };
  },
  methods: {
    initForm() {
      this.searchForm.first_name = '';
      this.searchForm.last_name = '';
      this.searchForm.middle_initial = '';
      this.handle = '';
      this.tweet_num = '50';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        first_name: this.searchForm.first_name,
        last_name: this.searchForm.last_name,
        middle_initial: this.searchForm.middle_initial,
        handle: this.searchForm.handle,
        tweet_num: this.searchForm.tweet_num,
      };
      this.first_name = this.searchForm.first_name;
      this.last_name = this.searchForm.last_name;
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
          this.getTweets();
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
    getTweets() {
      const path = 'http://localhost:5000/tweets';
      axios.get(path)
        .then((res) => {
          this.tweets = res.data;
          // eslint-disable-next-line
          console.log(this.tweets)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
    toggleSearch() {
      this.show_search = true;
    },
  },
  // created() {
  //   this.getMessage();
  // },
};
</script>
