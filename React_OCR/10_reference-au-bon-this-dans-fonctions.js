// ATTENTION AUX FONCTIONS FLÉCHÉES
<AwesomeConfirm onConfirm={() => this.triggerAwesome()} />
{
    items.map(item => (
        <CoolItem key={item.id} item={item} onEdit={() => this.editItem(item)} />
    ))
}
// Le problème ici est qu’à chaque render() produisant cette grappe, on crée de nouvelles fonctions
// pour les passer aux props: outre le coût de création et d’occupation mémoire associé, les composants
// ainsi paramétrés ont l’impression de recevoir des props différentes à chaque fois. Elles considéreront qu’ils devront
// re-renderer eux-mêmes, y compris lorsque cela est en fait superflu.
// Dans le second cas ci-dessus, la fonction fléchée à la volée est compréhensible, puisque l’appel de la méthode métier
// requiert une donnée fournie par la closure (ici le contexte en cours dans la fonction de rappel passée à map, pour aller y chercher item).
// Or, dans le premier cas, la fonction fléchée n’est qu’un passe-plat: elle n’apporte aucun élément de contexte supplémentaire
// à la méthode métier invoquée.
// 3 approches:

// 1 - bind DANS LE CONSTRUCTEUR
// Consiste à faire en sorte que chaque fois que notre propre composant est instancié, il se dote de ses propres « variantes »
// de la méthode. Ces variantes lui sont alors explicitement associées, c’est-à-dire qu’elles l’utiliseront toujours en tant que this.
class LoginScreen extends Component {
    constructor(props) {
        super(props)
        this.logIn = this.logIn.bind(this)
    }
  
    // …
}

// 2 - INITIALISEUR DE CHAMP
class LoginScreen extends Component {
    logIn = (event) => {
        // …
    }
  
    // …
}
// équivaut à:
class LoginScreen extends Component {
    constructor(props) {
        super(props)
        this.logIn = (event) => {
            // …
        }
    }
  
    // …
}
// Vu que les fonctions fléchées n’ont pas de contexte d’invocation, et notamment pas leur propre this mais celui le plus proche
// défini dans les portées englobantes (les closures), une telle méthode utilise bien le this en vigueur au niveau du constructeur.

// 3 - @autobind
import autobind from 'autobind-decorator'

// …

class LoginScreen extends Component {
    @autobind
    logIn(event) {
        // …
    }

    // …
}
// Syntaxe précise, simulable avec babel.