// PROPTYPES
// React examine sur tout composant une propriété statique, propTypes.
// C’est un objet dont les clés sont les noms des props attendues, et les valeurs des validateurs de props.
// Le module standard prop-types fournit une série de validateurs basés essentiellement 
// sur le type de valeur de base (nombre, texte, booléen, fonction de rappel…)
// et des agencements plus complexes (tableaux, objets, énumérations de valeurs ou types possibles…).
// Exemple:
import PropTypes from 'prop-types'

// …

Gauge.propTypes = {
    max: PropTypes.number,
    value: PropTypes.number.isRequired,
}

