import { useEffect, useState } from "react"
import api from "../api"
import "../styles/ProductSummary.css";

function ProductSummary(){
    const [products, setProducts] = useState([])
    const [nextPage, setNextPage] = useState(null)

    useEffect (() => {
        getProductList();
    }, [])

    const getProductList = () => {
        api.get("api/product/").then((res) => {
            setProducts(res.data.results);
            setNextPage(res.data.next);
        }).catch((err) => console.log(err));
    }

    return (
        <div className="product-summaries">
            {products.map((product) => (
                <div className="product-summary-container">
                    <img className="product-summary-image" src={product.image_url} alt={product.name}/>
                    <p className="product-summary-name">{product.name}</p>
                    <p className="product-summary-price">${product.price}</p>
                </div>
            ))}
        </div>
    )
}

export default ProductSummary