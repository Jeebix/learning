// La principale limite des fonctions, c’est qu’elles se restreignent en fait au rendu,
// c’est-à-dire à la constitution du DOM virtuel du composant, avec pour seule information entrante
// la liste des props issue du parent.
// Si nous avons besoin de préserver des informations d’un rendu à l’autre, cette approche ne suffit plus.
// Il est en effet impossible d’utiliser un état local sur un composant défini par une simple fonction.

// RAPPELS
// Définition de classe :
class Person {
    constructor(first, last) {
        this.first = first
        this.last = last
    }
  
    fullName() {
        return `${this.first} ${this.last}`
    }
}
// Si classe en spécialise une autre :
class CoolComponent extends Component {
    constructor(props) {
        super(props)
        this.state = { collapsed: props.initialCollapsed }
    }
  
    render() {
      // …
    }
}

// INTÉGRER defaultProps ET propTypes
// En haut de la classe, avec la propriété 'static'.
class CoolComponent extends Component {
    static defaultProps = {
        initialCollapsed: false,
    }
  
    static propTypes = {
        initialCollapsed: PropTypes.bool.isRequired,
        items: PropTypes.arrayOf(CoolItemPropType).isRequired,
    }
  
    constructor(props) {
        super(props)
        this.state = { collapsed: props.initialCollapsed }
    }
  
    render() {
      // …
    }
}

// UN MOT SUR createClass
// Avant ES2015, React avait besoin d'un mécanisme à lui pour créer une classe.
// API dépréciée aujourd'hui.
// Avec React.createClass, toutes es méthodes définies étaient auto-bound, c’est-à-dire que this
// y désignait toujours, par défaut, l’instance du composant.
// Avec les classes ES2015, il nous appartient de décider au cas par cas, pour nos méthodes, celles qui nécessitent
// un binding garanti, et de prendre les mesures nécessaires pour cela.