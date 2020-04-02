export default {
  data() {
    return {
      blue: 'rgb(20, 150, 230)',
      purple: 'rgb(200, 100, 235)',
      green: 'rgb(0, 255, 0)',
      yellow: 'rgb(230, 230, 0)',
      orange: 'rgb(255, 80, 0)',
      red: 'rgb(255, 20, 0)',
      grey: 'rgb(179, 181, 198)',
      white: 'rgb(255, 255, 255)',
    }
  },
  methods: {
    getColorWithAlpha(color, alpha) {
      return color.replace('rgb', 'rgba').replace(')', ', ' + alpha + ')');
    },
  }
};