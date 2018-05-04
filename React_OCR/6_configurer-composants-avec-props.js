// COMPOSANTS PARENTS ET ENFANTS
// Composant qui fournit le render() : parent
// Tout composant figurant dans ce render() : enfant
// 2 règles :
//     - Une prop est toujours passée par un composant parent à son composants enfants :
//       c’est le seul moyen normal de transmission;
//     - Une prop est considérée en lecture seule dans le composant qui la reçoit.

// PROPS TECHNIQUES
// React définit 3 props techniques:

    // key
    // Cela permet à React de gérer au mieux l’évolution du tableau d’un render() à l’autre.
    // L’absence de cette prop entraîne un avertissement en mode développement. Par ailleurs,
    // elle n'est pas consultable par le composant enfant qui la reçoit: elle ne figure pas dans sa liste de props.

    // children
    // Elle n’est pas fournie à l’aide d’un attribut, mais en imbriquant des composants à l’intérieur
    // du composant concerné. La liste des composants imbriqués constitue alors la prop children du composant
    // qui les « entoure ». Elle est donc automatiquement renseignée.
    return (
        <FileList>
          <UploadCreator />
          <StatusBar />
        </FileList>
    )
    // La prop children du composant <FileList /> est un tableau contenant <UploadCreator /> et <StatusBar />.
    // Children peut également être une fonction, ce qui permet l’injection localisée de dépendance
    // par le composant concerné.

    // dangerouslySetInnerHTML
    // Dernier recours: injection balisage manuel dans une grappe React.
    // Requiert en valeur une propriété __html dont la valeur est le balisage voulu.
    function createMarkup() {
        return { __html: 'First &middot; Second' }
    }
      
    function MyComponent() {
        return <div dangerouslySetInnerHTML={createMarkup()} />
    }

// VALEURS PAR DÉFAUT
// Composant peut définir des valeurs par défaut pour ses props.
function MyCoolComponent({ l10n, name, required, value }) {
    // …
}
  
MyCoolComponent.defaultProps = {
    l10n: true,
    required: false,
}