<template>
  <b-container>
    <div class="container">
      <!-- <b-button v-b-modal.searchmodal> Search </b-button> -->
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="First Name"
                      label-for="form-name-input">
            <b-form-input id="form-first-name-input"
                          type="text"
                          v-model="searchForm.first_name"
                          required
                          placeholder="Enter first name">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-name-group"
                        label="Last name:"
                        label-for="form-name-input">
              <b-form-input id="form-last-name-input"
                            type="text"
                            v-model="searchForm.last_name"
                            required
                            placeholder="Enter last name">
              </b-form-input>
            </b-form-group>
          <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="searchForm.alive" id="form-checks">
              <b-form-checkbox value="true">Alive?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger" @reset="onReset">Reset</b-button>
        </b-form>
      </div>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserSearch',
  data() {
    return {
      msg: 'Stuff!',
      searchForm: {
        first_name: '',
        last_name: '',
        alive: [],
      },
    };
  },
  methods: {
    initForm() {
      this.searchForm.first_name = '';
      this.searchForm.last_name = '';
      this.searchForm.alive = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        first_name: this.searchForm.first_name,
        last_name: this.searchForm.last_name,
        alive: this.searchForm.alive, // property shorthand
      };
      this.sendSearch(payload);
      this.initForm();
    },
    sendSearch(payload) {
      const path = 'http://localhost:5000/search';
      axios.post(path, payload)
        .then((response) => {
          // eslint-disable-next-line
          console.log(response.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
      // eslint-disable-next-line
      console.log("Reset")
    },
  },
  // created() {
  //   this.getMessage();
  // },
};
</script>
