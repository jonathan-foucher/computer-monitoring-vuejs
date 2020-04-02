export default {
  methods: {
    arrayAverage(array) {
      var sum = 0;
      for(var i = 0; i < array.length; i++) {
        sum += array[i];
      }
      return sum / array.length;
    },
  }
};