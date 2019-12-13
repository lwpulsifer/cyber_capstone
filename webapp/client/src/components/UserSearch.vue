<template>
  <b-container fluid>
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
          <b-form-input id="form-num_tweets-input"
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
        <h2>{{ first_name }} {{ last_name }}</h2>
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
    <b-col v-if="auth_count >= auth_threshold">
      <b-table class='tables'
          sticky-header='400px'
          bordered striped hover
          :items='tweets'></b-table>
    </b-col>
    <b-col v-else>
    <b-table-simple sticky-header='400px'>
      <b-th> Authentication Questions: Which one of these is your Tweet? </b-th>
      <b-tr>
        <question :possibles="question"
        :c="correct"
        @answer-clicked="answerClicked">
        </question>
      </b-tr>
    </b-table-simple>
    </b-col>
    </b-row>
    <div class="back-to-search">
      <b-button v-on:click="toggleSearch"> Return to Search </b-button>
      <b-button v-on:click="incAuth"> inc Auth </b-button>
    </div>
  </b-container>
  </b-container>
</template>

<script>
import axios from 'axios';
import question from './question.vue';

const NProgress = require('nprogress');

export default {
  name: 'UserSearch',
  components: {
    question,
  },
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
      question: [],
      correct: '',
      auth_count: 0,
      auth_threshold: 2,
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
        .then(() => {
          NProgress.done();
          this.getMessage();
          this.getTweets();
          this.authenticateTweets();
          this.show_search = false;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    authenticateTweets() {
      const path = 'http://localhost:5000/tweet_auth';
      axios.get(path)
        .then((res) => {
          this.question = res.data[0].possibles;
          this.correct = res.data[0].correct;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
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
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
    toggleSearch() {
      this.show_search = !this.show_search;
    },
    incAuth() {
      this.auth_count += 1;
    },
    answerClicked(e) {
      // eslint-disable-next-line
      console.log(e);
      if (e === 'correct') {
        this.incAuth();
      }
      this.authenticateTweets();
    },
  },
  // created() {
  //   this.getMessage();
  // },
};
</script>
