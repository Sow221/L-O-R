<!DOCTYPE html>
<html>
<head>
  <title>TensorFlow JavaScript - Prédiction MPG</title>
  <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.0.0/dist/tf.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-vis@1.8.0/dist/tfjs-vis.umd.min.js"></script>
  <style>
    body { font-family: Arial; margin: 20px; }
    h2 { color: #333; }
    .container { max-width: 1200px; margin: 0 auto; }
    #plot1, #plot2 { margin: 20px 0; border: 1px solid #ddd; padding: 10px; }
  </style>
</head>
<body>

<div class="container">
  <h2>🚀 TensorFlow JavaScript - Prédiction Efficacité Automobile</h2>
  <h3>Données d'entraînement :</h3>
  <p>Prédire MPG (Miles Per Gallon) à partir de la Puissance (Horsepower)</p>
  
  <div id="plot1"></div>
  <h3>Perte d'entraînement :</h3>
  <div id="plot2"></div>
</div>

<script>

// ═══════════════════════════════════════════════════════════════════════════════
// ÉTAPE 1 : COLLECTE DE DONNÉES - Extraire les bonnes données
// ═══════════════════════════════════════════════════════════════════════════════

function extractData(obj) {
  return {x: obj.Horsepower, y: obj.Miles_per_Gallon};
}

function removeErrors(obj) {
  return obj.x != null && obj.y != null;
}

console.log('✅ ÉTAPE 1 : Collecte de données');
console.log('   Extraction : Horsepower → X, Miles_per_Gallon → y');

// ═══════════════════════════════════════════════════════════════════════════════
// FONCTION : Affichage des données avec tfvis
// ═══════════════════════════════════════════════════════════════════════════════

function tfPlot(values, surface) {
  tfvis.render.scatterplot(surface,
    {values: values, series: ['Original', 'Predicted']},
    {xLabel: 'Horsepower (ch)', yLabel: 'MPG (mile/gallon)'}
  );
}

// ═══════════════════════════════════════════════════════════════════════════════
// FONCTION PRINCIPALE : Orchestration complète du pipeline
// ═══════════════════════════════════════════════════════════════════════════════

async function runTF() {
  console.log('\n═'.repeat(80));
  console.log('  🤖 PIPELINE TENSORFLOW - DÉBUT');
  console.log('═'.repeat(80));
  
  // ─────────────────────────────────────────────────────────────────────────────
  // Charger les données
  // ─────────────────────────────────────────────────────────────────────────────
  console.log('\n📊 Chargement des données...');
  const jsonData = await fetch("cardata.json");
  let values = await jsonData.json();
  values = values.map(extractData).filter(removeErrors);
  console.log(`   ✅ ${values.length} exemples chargés`);
  
  // ─────────────────────────────────────────────────────────────────────────────
  // ÉTAPE 2 : TRAITEMENT DES DONNÉES - Normalisation
  // ─────────────────────────────────────────────────────────────────────────────
  console.log('\n✅ ÉTAPE 2 : Traitement des données');
  
  // Créer les tensors
  const inputs = values.map(obj => obj.x);
  const labels = values.map(obj => obj.y);
  const inputTensor = tf.tensor2d(inputs, [inputs.length, 1]);
  const labelTensor = tf.tensor2d(labels, [labels.length, 1]);
  
  // Trouver min/max
  const inputMin = inputTensor.min();  
  const inputMax = inputTensor.max();
  const labelMin = labelTensor.min();
  const labelMax = labelTensor.max();
  
  // Normaliser entre 0 et 1
  const nmInputs = inputTensor.sub(inputMin).div(inputMax.sub(inputMin));
  const nmLabels = labelTensor.sub(labelMin).div(labelMax.sub(labelMin));
  
  console.log('   Normalisation : [0, 1]');
  console.log(`   Horsepower : [${inputMin.dataSync()[0].toFixed(1)}, ${inputMax.dataSync()[0].toFixed(1)}]`);
  console.log(`   MPG : [${labelMin.dataSync()[0].toFixed(1)}, ${labelMax.dataSync()[0].toFixed(1)}]`);
  
  // Afficher les données originales
  const surface1 = document.getElementById("plot1");
  const surface2 = document.getElementById("plot2");
  tfPlot(values, surface1);
  
  // ─────────────────────────────────────────────────────────────────────────────
  // ÉTAPE 3 : CRÉATION D'UN MODÈLE - Architecture
  // ─────────────────────────────────────────────────────────────────────────────
  console.log('\n✅ ÉTAPE 3 : Création d\'un modèle');
  
  const model = tf.sequential({
    layers: [
      // Couche 1 : Dense avec activation ReLU
      tf.layers.dense({
        inputShape: [1],     // 1 entrée (Horsepower)
        units: 50,           // 50 neurones
        activation: 'relu',  // ReLU : f(x) = max(0, x)
        useBias: true
      }),
      
      // Couche 2 : Dense avec activation ReLU
      tf.layers.dense({
        units: 1             // 1 sortie (MPG)
      })
    ]
  });
  
  console.log('   Architecture : [1] → [50] → [1]');
  console.log('   Couche 1 : Dense 1→50 (ReLU)');
  console.log('   Couche 2 : Dense 50→1 (Linear)');
  
  // ─────────────────────────────────────────────────────────────────────────────
  // ÉTAPE 4 : COMPILATION DU MODÈLE
  // ─────────────────────────────────────────────────────────────────────────────
  console.log('\n✅ ÉTAPE 4 : Compilation du modèle');
  
  model.compile({
    loss: 'meanSquaredError',
    optimizer: tf.train.adam(0.01)
  });
  
  console.log('   Loss : Mean Squared Error');
  console.log('   Optimizer : Adam (learning_rate=0.01)');
  
  // ─────────────────────────────────────────────────────────────────────────────
  // ÉTAPE 5 : ENTRAÎNEMENT DU MODÈLE
  // ─────────────────────────────────────────────────────────────────────────────
  console.log('\n✅ ÉTAPE 5 : Entraînement du modèle');
  
  await trainModel(model, nmInputs, nmLabels, surface2);
  
  // ─────────────────────────────────────────────────────────────────────────────
  // ÉTAPE 6 : UTILISATION DU MODÈLE - Dénormalisation et prédictions
  // ─────────────────────────────────────────────────────────────────────────────
  console.log('\n✅ ÉTAPE 6 : Utilisation du modèle');
  
  // Générer des prédictions sur la plage [0, 1]
  let unX = tf.linspace(0, 1, 100);      
  let unY = model.predict(unX.reshape([100, 1]));      
  
  // Dénormaliser X
  const unNormunX = unX
    .mul(inputMax.sub(inputMin))
    .add(inputMin);
  
  // Dénormaliser Y
  const unNormunY = unY
    .mul(labelMax.sub(labelMin))
    .add(labelMin);
  
  unX = unNormunX.dataSync();
  unY = unNormunY.dataSync();
  
  console.log('   Dénormalisation réussie');
  console.log('   100 prédictions générées');
  
  // Créer les prédictions
  const predicted = Array.from(unX).map((val, i) => {
    return {x: val, y: unY[i]}
  });
  
  // Afficher données originales + prédictions
  tfPlot([values, predicted], surface1);
  console.log('   ✅ Graphiques mis à jour');
  
  // ─────────────────────────────────────────────────────────────────────────────
  // Nettoyage mémoire
  // ─────────────────────────────────────────────────────────────────────────────
  inputTensor.dispose();
  labelTensor.dispose();
  nmInputs.dispose();
  nmLabels.dispose();
  
  console.log('\n' + '═'.repeat(80));
  console.log('  ✅ PIPELINE TENSORFLOW - TERMINÉ');
  console.log('═'.repeat(80) + '\n');
}

// ═══════════════════════════════════════════════════════════════════════════════
// FONCTION D'ENTRAÎNEMENT - Boucle d'apprentissage
// ═══════════════════════════════════════════════════════════════════════════════

async function trainModel(model, inputs, labels, surface) {
  console.log('\n   Démarrage de l\'entraînement...');
  
  const batchSize = 25;      // Traiter 25 exemples à la fois
  const epochs = 50;          // 50 itérations complètes
  
  // Callbacks pour visualiser la perte
  const callbacks = tfvis.show.fitCallbacks(
    surface, 
    ['loss'], 
    {callbacks: ['onEpochEnd']}
  );
  
  const history = await model.fit(inputs, labels, {
    batchSize: batchSize,
    epochs: epochs,
    shuffle: true,
    callbacks: callbacks,
    verbose: 0
  });
  
  console.log(`   Epochs : ${epochs}`);
  console.log(`   Batch Size : ${batchSize}`);
  console.log(`   ✅ Entraînement terminé !`);
  
  return history;
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXÉCUTION PRINCIPALE
// ═══════════════════════════════════════════════════════════════════════════════

runTF();

</script>

</body>
</html>
