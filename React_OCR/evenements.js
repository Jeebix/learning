// React nous permet de déclarer nos gestionnaires à même le code JSX de notre composant,
// tout en optimisant en interne sa gestion événementielle, avec au plus un gestionnaire réel
// par type d’événement dans une grappe applicative React. On conserve la lisibilité immédiate
// du côté « déclaration de gestionnaire à la volée » sans sacrifier pour autant la performance.
// Et pour nous le proposer, et ce quel que soit le type d’événement souhaité, il simule la propagation
// lorsque celle-ci n’est pas native.

const Greeter = ({ whom }) => (
    <button onClick={() => console.log(`Bonjour ${whom} !`)}>
      Vas-y, clique !
    </button>
)
ReactDOM.render(<Greeter whom="Roberto" />, document.getElementById('root'))
//  Cliquer sur le bouton obtenu affichera un « Bonjour Roberto ! » dans la console du navigateur.

class LogEntry extends Component {
    // …
    render() {
        const className = `log entry ${this.isOpen() ? 'open' : 'closed'}`
        return (
            <li className={className} onClick={this.toggle}>
            …
            </li>
        )
    }
}
// Pratique de voir, à même le JSX, qu’on va réagir aux clics sur la ligne et que ce sera avec la méthode toggle(…)
// du composant.



