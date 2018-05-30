import React from 'react'
import PropTypes from "prop-types";

import './Card.css'

// Jeu de Memory: composant de base affiché est la carte, soit visible, soit de dos (masquée).
// Composant Card reçoit 2 props: card, symbole à afficher + feedback, l'état visuel de la carte.

const HIDDEN_SYMBOL = '❓'

const Card = ({ card, feedback, index, onClick }) => (
    <div className={`card ${feedback}`} onClick={() => onClick(index)}>
        <span className="symbol">
            {feedback === 'hidden' ? HIDDEN_SYMBOL : card}
        </span>
    </div>
)

export default Card

Card.propTypes = {
    card: PropTypes.string.isRequired,
    feedback: PropTypes.oneOf([
      'hidden',
      'justMatched',
      'justMismatched',
      'visible',
    ]).isRequired,
    index: PropTypes.number.isRequired,
    onClick: PropTypes.func.isRequired,
}
// oneOf pour énumération.

// On déstructure directement les props passées en arguments (un gros objet de props).

// Étant donné que la fonction renvoie directement une grappe de DOM virtuel, sans calcul préalable,
// on se dispense des accolades de bloc et du return, pour renvoyer directement l’expression : on trouve donc plutô
// des parenthèses autour du JSX.

// La syntaxe de valeur textuelle pour une prop ne permet pas l’interpolation (c'est-à-dire l’incrustation
// de contenu dynamique dans le texte). On a donc recours pour le <div> principal à une expression JSX (entre accolades
// qui, elle, peut utiliser la syntaxe des template strings d’ES2015, entre backquotes (`), pour incruster dynamiquement
// la valeur de feedback.
