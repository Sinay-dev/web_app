<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import fastapiLogo from './assets/fastapilogo.png'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div>
    <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">
      <img src={fastapiLogo} class="logo" alt="fastapiLogo Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>FastAPI + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Site web déployé par Yanis Bensadok, voici mon <a href=" " target= "_blank" rel="noreferrer">code</a>
  </p>

  <p class="read-the-docs">
    J'ai déployé ce site pour montrer que tout seul j'ai pu me débrouiller pour apprendre à utiliser les différents services de GCP pour déployer une application web.
  </p>
  <p class="read-the-docs">
    Je prévois de transformer ce site en portfolio cette semaine et d'inclure les étapes à suivre pour le déployer.
  </p>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
