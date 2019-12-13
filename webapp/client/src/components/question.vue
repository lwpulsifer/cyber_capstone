<template>
<div>
  <b-table :items="possibles" @row-clicked="handleClick"></b-table>
</div>
</template>
<script>
export default {
  name: 'Question',
  props: ['possibles', 'c'],
  data() {
    return {
      answer: 'Howdy',
    };
  },
  methods: {
    handleClick(record) {
      this.authenticateTweet(record, this.c);
    },
    authenticateTweet(record, correct) {
      // Would check server in a more secure paradigm
      // eslint-disable-next-line
      console.log(record)
      // eslint-disable-next-line
      console.log(correct)
      if (record.Question === correct) {
        // eslint-disable-next-line
        this.$emit('answer-clicked', 'correct');
      } else {
        this.$emit('answer-clicked', 'wrong');
      }
      return true;
    },
  },
};
</script>
