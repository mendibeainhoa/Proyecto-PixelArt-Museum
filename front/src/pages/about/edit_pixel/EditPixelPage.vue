
<template>
    <div class="container">
    <div style="float:left; width:800px">
        <Art :colors="colors" />
    </div>
    <div style="float: right; width:300px; margin-top:200px">
        <chrome-picker v-model="colors" />
    </div>
    
    </div>
</template>
<script>
import Art from './Art.vue';
import { Chrome } from 'vue-color'
export default {
data(){
        return {
            colors: []
        }
    },
methods: {
        changeColor(){
            console.log('Change color');
            this.coloring = colors.hex;
        }
    },
components: {
        Art,
        'chrome-picker': Chrome
    }
}
</script>