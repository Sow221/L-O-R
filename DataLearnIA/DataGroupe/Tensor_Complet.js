/*
═══════════════════════════════════════════════════════════════════════════════
                    PROJET TENSOR - RÉSEAU DE NEURONES
═══════════════════════════════════════════════════════════════════════════════

Créer un modèle de réseau de neurones avec TensorFlow.js pour prédire 
les prix de maisons basé sur la superficie et le nombre de pièces.

ÉTAPES :
1. Collecte de données
2. Création d'un modèle séquentiel
3. Ajout de couches (Dense, activation)
4. Compilation du modèle
5. Entraînement du modèle
6. Utilisation pour prédictions

À utiliser dans un navigateur avec TensorFlow.js CDN :
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.0.0"></script>
*/

// ═══════════════════════════════════════════════════════════════════════════════
// ÉTAPE 1 : COLLECTE DE DONNÉES
// ═══════════════════════════════════════════════════════════════════════════════

console.log('═'.repeat(80));
console.log('  🚀 PROJET TENSOR - RÉSEAU DE NEURONES');
console.log('═'.repeat(80));

// Données d'entraînement : [superficie (m²), nombre de pièces] → prix (€)
const donnees = [
  { X: [100, 2], y: 150000 },
  { X: [150, 3], y: 250000 },
  { X: [200, 4], y: 350000 },
  { X: [120, 2], y: 180000 },
  { X: [180, 3], y: 300000 },
  { X: [250, 4], y: 450000 },
  { X: [80, 1], y: 100000 },
  { X: [300, 5], y: 550000 },
  { X: [140, 3], y: 220000 },
  { X: [220, 4], y: 380000 }
];

// Extraire X (features) et y (target)
const X = tf.tensor2d(donnees.map(d => d.X));
const y = tf.tensor2d(donnees.map(d => [d.y]), [donnees.length, 1]);

console.log('\n✅ ÉTAPE 1 : COLLECTE DE DONNÉES');
console.log(`   Nombre d'exemples : ${donnees.length}`);
console.log(`   Features X (shape) : [${X.shape}]`);
console.log(`   Target y (shape) : [${y.shape}]`);
console.log('   Structure : [superficie, nb_pièces] → prix');

// ═══════════════════════════════════════════════════════════════════════════════
// ÉTAPE 2 : CRÉATION D'UN MODÈLE SÉQUENTIEL
// ═══════════════════════════════════════════════════════════════════════════════

const model = tf.sequential({
  layers: []  // Les couches seront ajoutées dans l'étape 3
});

console.log('\n✅ ÉTAPE 2 : CRÉATION D\'UN MODÈLE SÉQUENTIEL');
console.log('   Type : Sequential (couches empilées linéairement)');
console.log('   Architecture : Input → Dense → Dense → Output');

// ═══════════════════════════════════════════════════════════════════════════════
// ÉTAPE 3 : AJOUT DE COUCHES AU MODÈLE
// ═══════════════════════════════════════════════════════════════════════════════

// Couche 1 : Dense avec activation ReLU
model.add(
  tf.layers.dense({
    inputShape: [2],        // 2 entrées : [superficie, nb_pièces]
    units: 8,               // 8 neurones cachés
    activation: 'relu'      // Activation ReLU : f(x) = max(0, x)
  })
);

// Couche 2 : Dense avec activation ReLU
model.add(
  tf.layers.dense({
    units: 4,               // 4 neurones
    activation: 'relu'
  })
);

// Couche 3 : Dense de sortie (régression linéaire)
model.add(
  tf.layers.dense({
    units: 1                // 1 sortie : le prix prédit
  })
);

console.log('\n✅ ÉTAPE 3 : AJOUT DE COUCHES AU MODÈLE');
console.log('   Couche 1 (Dense) : inputShape=[2] → units=8, activation=relu');
console.log('   Couche 2 (Dense) : units=4, activation=relu');
console.log('   Couche 3 (Sortie) : units=1, activation=linear (régression)');
console.log('\n   Architecture : [2] → [8] → [4] → [1]');
console.log('   Paramètres :');
console.log('     • Poids couche 1 : 2×8 = 16 + biais = 17');
console.log('     • Poids couche 2 : 8×4 = 32 + biais = 36');
console.log('     • Poids couche 3 : 4×1 = 4 + biais = 5');
console.log('     • Total : 58 paramètres à apprendre');

// ═══════════════════════════════════════════════════════════════════════════════
// ÉTAPE 4 : COMPILATION DU MODÈLE
// ═══════════════════════════════════════════════════════════════════════════════

model.compile({
  optimizer: tf.train.adam(0.01),   // Optimiseur Adam avec learning rate = 0.01
  loss: 'meanSquaredError',         // MSE pour régression
  metrics: ['mae']                  // Métrique : Mean Absolute Error
});

console.log('\n✅ ÉTAPE 4 : COMPILATION DU MODÈLE');
console.log('   Optimiseur : Adam (adaptive moment estimation)');
console.log('   Learning Rate : 0.01');
console.log('   Fonction de perte : meanSquaredError (MSE)');
console.log('   Métrique : mae (Mean Absolute Error)');
console.log('\n   Résumé du modèle :');
model.summary();

// ═══════════════════════════════════════════════════════════════════════════════
// ÉTAPE 5 : ENTRAÎNEMENT DU MODÈLE
// ═══════════════════════════════════════════════════════════════════════════════

console.log('\n✅ ÉTAPE 5 : ENTRAÎNEMENT DU MODÈLE');

(async function() {
  try {
    // Entraîner le modèle
    const history = await model.fit(X, y, {
      epochs: 100,           // 100 itérations complètes sur les données
      batchSize: 2,          // Traiter 2 exemples à la fois
      verbose: 0,            // Pas d'affichage en temps réel (verbose: 1 pour voir)
      shuffle: true,         // Mélanger les données
      validationSplit: 0.2   // 20% pour validation
    });
    
    console.log('   Entraînement terminé !');
    console.log(`   Nombre d'epochs : 100`);
    console.log(`   Batch size : 2`);
    
    const losses = history.history.loss;
    console.log(`\n   Perte initiale : ${losses[0].toFixed(6)}`);
    console.log(`   Perte finale : ${losses[99].toFixed(6)}`);
    console.log(`   Amélioration : ${((losses[0] - losses[99]) / losses[0] * 100).toFixed(1)}%`);
    
    // ═══════════════════════════════════════════════════════════════════════════════
    // ÉTAPE 6 : UTILISATION DU MODÈLE POUR PRÉDICTIONS
    // ═══════════════════════════════════════════════════════════════════════════════
    
    console.log('\n✅ ÉTAPE 6 : UTILISATION DU MODÈLE POUR PRÉDICTIONS');
    
    // Prédictions sur les données d'entraînement
    const predictions = model.predict(X);
    const pred_array = predictions.dataSync();
    
    console.log('\n📊 COMPARAISON : PRIX RÉEL vs PRIX PRÉDIT (5 premiers exemples)');
    console.log('   ────────────────────────────────────────────────────────────');
    console.log('   m²  | Pièces | Prix Réel  | Prix Prédit | Erreur   | %');
    console.log('   ────────────────────────────────────────────────────────────');
    
    let erreur_totale = 0;
    for (let i = 0; i < Math.min(5, donnees.length); i++) {
      const real = donnees[i].y;
      const pred = pred_array[i];
      const error = Math.abs(real - pred);
      const error_percent = (error / real * 100).toFixed(1);
      
      console.log(`   ${String(donnees[i].X[0]).padEnd(3)} | ${String(donnees[i].X[1]).padEnd(6)} | ${String(real).padEnd(10)} | ${String(pred.toFixed(0)).padEnd(11)} | ${String(error.toFixed(0)).padEnd(8)} | ${error_percent}%`);
      erreur_totale += error;
    }
    
    const moy_erreur = erreur_totale / Math.min(5, donnees.length);
    console.log(`\n   Erreur moyenne : ${moy_erreur.toFixed(0)}€`);
    
    // ═══════════════════════════════════════════════════════════════════════════════
    // PRÉDICTIONS SUR NOUVELLES DONNÉES
    // ═══════════════════════════════════════════════════════════════════════════════
    
    console.log('\n' + '═'.repeat(80));
    console.log('  🔮 PRÉDICTIONS SUR NOUVELLES DONNÉES');
    console.log('═'.repeat(80));
    
    const testCases = [
      { superficie: 175, pieces: 3, description: 'Petit maison familiale' },
      { superficie: 280, pieces: 4, description: 'Grande maison' },
      { superficie: 90, pieces: 1, description: 'Studio/petit appart' }
    ];
    
    for (let i = 0; i < testCases.length; i++) {
      const testCase = testCases[i];
      const input = tf.tensor2d([[testCase.superficie, testCase.pieces]]);
      const prediction = model.predict(input);
      const prix = prediction.dataSync()[0];
      
      console.log(`\n   ${i+1}. ${testCase.description}`);
      console.log(`      Superficie : ${testCase.superficie}m²`);
      console.log(`      Nombre de pièces : ${testCase.pieces}`);
      console.log(`      💰 Prix prédit : ${prix.toFixed(0)}€`);
      console.log(`      Prix au m² : ${(prix / testCase.superficie).toFixed(0)}€/m²`);
      
      input.dispose();
      prediction.dispose();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════════
    // LIBÉRATION DE LA MÉMOIRE
    // ═══════════════════════════════════════════════════════════════════════════════
    
    console.log('\n' + '═'.repeat(80));
    console.log('  ✅ PROJET TENSOR TERMINÉ !');
    console.log('═'.repeat(80));
    
    console.log('\n📚 RÉSUMÉ DU PROJET :');
    console.log('   ✓ Données collectées et préparées');
    console.log('   ✓ Modèle créé avec 3 couches');
    console.log('   ✓ Modèle compilé avec Adam optimizer');
    console.log('   ✓ Modèle entraîné sur 100 epochs');
    console.log('   ✓ Prédictions réussies sur nouvelles données');
    console.log('\n💡 PROCHAINES ÉTAPES :');
    console.log('   • Augmenter les données d\'entraînement');
    console.log('   • Ajouter de la régularisation (dropout)');
    console.log('   • Ajuster les hyperparamètres');
    console.log('   • Utiliser validation/test sets');
    console.log('   • Déployer le modèle');
    
    // Libérer la mémoire
    X.dispose();
    y.dispose();
    predictions.dispose();
    
  } catch (error) {
    console.error('❌ Erreur lors de l\'entraînement :', error);
  }
})();
