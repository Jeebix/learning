import React from 'react'
import PropTypes from "prop-types"

import './HallOfFame.css'

const HallOfFame = ({ entries }) => (
    <table className="hallOfFame">
        <tbody>
            {
                entries.map(({ date, guesses, id, player }) => (
                    <tr key={id}>
                        <td className="date">{date}</td>
                        <td className="guesses">{guesses}</td>
                        <td className="player">{player}</td>                        
                    </tr>
                ))
            }
        </tbody>
    </table>
)

export default HallOfFame

// == Internal helpers ==============================================

export const FAKE_HOF = [
    { id: 3, guesses: 18, date: '10/10/2017', player: 'Jane' },
    { id: 2, guesses: 23, date: '11/10/2017', player: 'Kevin' },
    { id: 1, guesses: 31, date: '06/10/2017', player: 'Louisa' },
    { id: 0, guesses: 48, date: '14/10/2017', player: 'Marc' },
]

HallOfFame.propTypes = {
    entries: PropTypes.arrayOf(
        PropTypes.shape({
            date: PropTypes.string.isRequired,
            guesses: PropTypes.number.isRequired,
            id: PropTypes.number.isRequired,
            player: PropTypes.string.isRequired
        })
    ).isRequired,
}
// arrayOf : indique que la prop sera un tableau de valeurs dont la définition est fournie en argument.
// shape : décrit un objet dont les clés sont connues, en précisant les types de leurs valeurs.