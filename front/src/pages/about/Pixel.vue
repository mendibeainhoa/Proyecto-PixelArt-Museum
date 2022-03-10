<template>
<div class="pixel" v-bind:style="{background: activeBackground}" @click="changeColor">
 </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Pixel');
        },
data(){
            return {
                activeBackground: '#ffffff'
            }
        },
methods: {
            changeColor(){
                if(this.activeBackground == this.coloring){
                    this.activeBackground = '#ffffff'
                }else{
                    this.activeBackground = this.coloring;
                }
                
            }
        },
props: [
         'coloring'
        ]
    }
</script>

<style scoped>   
    div.pixel{
        /*border: 1px solid #000;*/
        height: 20px;
        width: 20px;
        float: left;
    }
</style>