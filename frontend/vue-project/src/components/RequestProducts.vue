<script setup lang="ts">
import { ref, onMounted } from 'vue';

const userContent = ref<string>('Loading...');

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8001/');
    userContent.value = await res.text();
  } catch (error) {
    userContent.value = 'Error fetching data from msvc-products service';
  }
});
</script>

<template>
  <div>
    <p>{{ userContent }}</p>
  </div>
</template>