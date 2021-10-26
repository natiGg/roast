<template>
  <div>
    <Navigation/>
    <Hero/>
    <Feature/>
    <Footer/>
  </div>

</template>

<script>
import Navigation from '@/components/Navigation.vue'
import Hero from '@/components/Hero.vue'
import Footer from '@/components/Footer.vue'
import Feature from '@/components/Feature.vue'

export default {
  data () {
    return {

    }
  },
  components: {
    Navigation,
    Hero,
    Feature,
    Footer
  }
}
</script>
