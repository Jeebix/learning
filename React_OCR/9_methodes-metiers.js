// TYPES DE MÉTHODES MÉTIER
// Dans nos composants définis par des classes, les méthodes sont de différentes natures :
// • Calculs et construction de données, qu’on souhaite par exemple sortir du render() pour que celui-ci
//   se concentre sur sa tâche principale : structurer le DOM virtuel.
// • Méthodes de cycle de vie (nous les verrons plus en détail dans le dernier chapitre de cette partie)
// • Gestionnaires d’événements; il est possible de les définir à la volée dans render(), mais lorsqu’ils
//   ne dépendent que de l’événement reçu, on préfèrera alors les extraire pour des raisons de performance.
