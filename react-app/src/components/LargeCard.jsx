export const LargeCard = ({header, mainStat, auxStatName1, auxStat1, auxStatName2, auxStat2, auxStatName3, auxStat}) => {

    return (
        <div className="card bg-dark">
            <div className="card-body">
                <h5 className="card-title">{header}</h5>
                <h6>{mainStat}</h6>
            </div>
        </div>
    )

}
