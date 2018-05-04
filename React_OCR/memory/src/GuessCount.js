import React from 'react'
import PropTypes from "prop-types"

import './GuessCount.css'

const GuessCount = ({ guesses }) => <div className="guesses">{guesses}</div>

export default GuessCount

GuessCount.propTypes = {
    guesses: PropTypes.number.isRequired,
}

// Composant GuessCount = compteur de tentatives.
// Au fil de la partie, on l'affiche avant le plateau de cartes.
