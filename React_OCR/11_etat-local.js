// Pour représenter les données qui persistent d’un render() à l’autre ou simplement re-déclenchent un rendu,
// React utilise l’état local des composants.

// OÙ EST SITUÉ L'ÉTAT LOCAL ?
// L'état local est présent à l'intérieur d'un composant, dans sa propriété 'state'.
// On doit obligatoirement utiliser une définition de composant par classe, et non une simple fonction.
// L’état par défaut est null, il faudra donc le plus souvent l’initialiser manuellement dans le constructeur,
// soit de manière explicite :
class Accordion extends Component {
    constructor(props) {
        super(props)
        this.state = { expandedPanels: new Set() }
    }
  
    // …
}
// Ou, implicitement, par un initialisateur de champ :
class Accordion extends Component {
    state = { expandedPanels: new Set() }
  
    // …
}

// QUI A ACCÈS À L'ÉTAT LOCAL ?
// Uniquement le composant, pas les parents ni enfants.
// En conséquence, si vous avez des éléments d’état à « partager » entre plusieurs composants, React vous demandera
// de « lift state », c’est-à-dire de faire remonter ces données vers l’état local du plus proche composant ancêtre commun
// dans la grappe, celui qui contient dans sa grappe l’ensemble des composants souhaitant « partager » l’info.
// Il vous appartiendra alors de :
//   • faire « redescendre » ces infos à coup de props jusqu’aux composants qui en ont besoin;
//   • faire « remonter » les demandes d’évolution à coup de props de type fonction, fournies par le composant doté de l’état local,
//     et utilisées par les composants qui en ont besoin.

    // Exemple
    // 1 accordéon avec des composants « panneau d’accordéon », qui gouvernent leur ouverture-fermeture, à ceci près
    // que l’accordéon doit permettre de tout ouvrir ou de tout refermer.
    // Le composant <AccordionPanel />, qui n’a donc pas d’état propre :
    function AccordionPanel({ item: { title, content }, open, onToggle }) {
        return (
            <section className="accordion-panel">
                <h1 className="accordion-header" onClick={() => onToggle(item)} />
                <div className="accordion-content">{content}</div>
            </section>
        )
    }
    AccordionPanel.defaultProps = {
        open: false,
    }
    AccordionPanel.propTypes = {
        item: ItemPropType.isRequired,
        open: PropTypes.bool,
        onToggle: PropTypes.func.isRequired,
    }
    // Ici, le panneau tire son contenu et son état (ouvert/fermé) de ses props, il n’a aucun état propre. Du coup, le traitement
    // de la demande de bascule ouvert/fermé est délégué à une fonction de rappel passée en prop, onToggle,
    // puisqu’il n’a rien « localement » qu’il puisse modifier pour changer son statut ouvert.
    // Au-dessus, on aurait un composant Accordéon qui ressemblerait à ceci :
    class Accordion extends Component {
        static propTypes = {
            items: PropTypes.arrayOf(ItemPropType).isRequired,
        }
      
        constructor(props) {
            super(props)
            this.state = { expandedPanels: new Set() }
        }
      
        render() {
            const { items } = this.props
            return (
                <div className="accordion">
                    {items.map((item) => (
                        <AccordionPanel
                            key={item.id}
                            item={item}
                            onToggle={this.togglePanel}
                            open={this.state.expandedPanels.has(item)}
                        />
                    ))}
                </div>
            )
        }
      
        // This method is declared using an arrow function initializer solely
        // to guarantee its binding, as we cannot use decorators just yet.
        togglePanel = (panel) => {
            const expandedPanels = this.state.expandedPanels
            if (expandedPanels.has(panel)) {
                expandedPanels.remove(panel)
            } else {
                expandedPanels.add(panel)
            }
            this.setState({ expandedPanels })
        }
    }
    // Le fait que l’accordéon gère lui-même les états ouvert/fermé de ses panneaux via sa variable d’état local expandedPanels,
    // et qu'il la met à jour non pas directement, mais à l’aide de setState().