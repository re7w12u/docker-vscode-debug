<script setup lang="ts">
import { ref, onMounted } from 'vue';

const userContent = ref<string>('Loading...');

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8002/');
    userContent.value = await res.text();
  } catch (error) {
    userContent.value = 'Error fetching data from msvc-user service';
  }
});
</script>

<template>
  <div>
    <p>{{ userContent }}</p>
  </div>
</template>