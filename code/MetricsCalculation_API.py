from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd


def support(df, endpoint):
    support = []
    for i, row in df.iterrows():
        body = row['Body']
        head = row['Head']
        body = body.replace('?a  <', '?a  LC:').replace('>  <', ' LCe:').replace('>', '.')
        head = head.replace('?a  <', '?a  LC:').replace('>  <', ' LCe:').replace('>', '.')

        prefix = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \n" + \
                 "PREFIX LC: <http://LungCancer.eu/vocab/> \n" + \
                 "PREFIX LCe: <http://LungCancer.eu/entity/> \n" + \
                 "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"

        query_select_clause = "SELECT (COUNT(DISTINCT *) AS ?Support) WHERE { \n " \
                              " SELECT ?a WHERE " \
                              "{  \n "
        query_where_clause = body + "\n" + head + "\n } } "

        sparqlQuery = prefix + "" + query_select_clause + " " + query_where_clause
        print(sparqlQuery)
        sparql = SPARQLWrapper(endpoint)
        sparql.setQuery(sparqlQuery)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        data = results["results"]["bindings"]
        support.append(data[0]["Support"]["value"])
    # print(support)
    return support



def confidence(df, endpoint):
    confidence = []
    for i, row in df.iterrows():
        body = row['Body']
        head = row['Head']
        body = body.replace('?a  <', '?a  LC:').replace('>  <', ' LCe:').replace('>', '.')
        head = head.replace('?a  <', '?a  LC:').replace('>  <', ' LCe:').replace('>', '.')

        prefix = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \n" + \
                 "PREFIX LC: <http://LungCancer.eu/vocab/> \n" + \
                 "PREFIX LCe: <http://LungCancer.eu/entity/> \n" + \
                 "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"

        query_select_clause_subquery1 = "SELECT (xsd:float(?PEHead)/xsd:float(?PFHead) AS ?Confidence) WHERE { \n" \
                              "{SELECT (COUNT(DISTINCT *) AS ?PEHead) WHERE { \n " \
                              "SELECT ?a WHERE { \n "
        query_where_clause_subquery1 = body + "\n" + head + "\n } } } \n"

        query_select_clause_subquery2 = "{SELECT (COUNT(DISTINCT *) AS ?PFHead) WHERE {\n "
        query_where_clause_subquery2 =  head + "\n } } } "



        sparqlQuery = prefix + "" + query_select_clause_subquery1 + " " + query_where_clause_subquery1 + "" + query_select_clause_subquery2 + " " + query_where_clause_subquery2
        # print(sparqlQuery)
        sparql = SPARQLWrapper(endpoint)
        sparql.setQuery(sparqlQuery)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        data = results["results"]["bindings"]
        confidence.append(data[0]["Confidence"]["value"])
    return confidence


def pca_confidence(df, endpoint):
    pca_confidence = []
    for i, row in df.iterrows():
        body = row['Body']
        head = row['Head']
        body = body.replace('?a  <', '?a  LC:').replace('>  <', ' LCe:').replace('>', '.')
        head = head.replace('?a  <', '?a  LC:').replace('>  <', ' LCe:').replace('>', '.')
        substring = 'LCe:'
        str_list = head.split(substring)[0]
        free_head = "".join(str_list)

        prefix = "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \n" + \
                 "PREFIX LC: <http://LungCancer.eu/vocab/> \n" + \
                 "PREFIX LCe: <http://LungCancer.eu/entity/> \n" + \
                 "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"

        query_select_clause_subquery1 = "SELECT (xsd:float(?Support)/xsd:float(?PCABodySize) AS ?PCA) WHERE { \n " \
                                        "{SELECT (COUNT(DISTINCT *) AS ?Support) WHERE { \n" \
                                        "SELECT ?a WHERE {\n "
        query_where_clause_subquery1 = body + "\n" + head + "\n } } } \n"

        query_select_clause_subquery2 = "{SELECT (COUNT(DISTINCT *) AS ?PCABodySize) WHERE { \n" \
                                        "SELECT ?a  WHERE {\n "
        query_where_clause_subquery2 =  body + "\n" + free_head + " ?b \n } } } }"

        sparqlQuery = prefix + "" + query_select_clause_subquery1 + " " + query_where_clause_subquery1 + "" + query_select_clause_subquery2 + " " + query_where_clause_subquery2

        sparql = SPARQLWrapper(endpoint)
        sparql.setQuery(sparqlQuery)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        data = results["results"]["bindings"]
        pca_confidence.append(data[0]["PCA"]["value"])
    return pca_confidence


def writeData(df,supp,conf,pca):
    df['Inferred_Support'] = supp
    df['Inferred_Confidence'] = conf
    df['Inferred_PCA'] = pca
    #  saving the metrics over KG with inferred triples
    df.to_csv("results/phd_experiments_result.csv", index=False)


def read():
    # Subset of rules for experiments
    df = pd.read_csv("phd_experiments.csv")
    # SPARQL endpoint of KG with inferred triples
    endpoint = "http://localhost:7000/repositories/exp"
    supp = support(df, endpoint)
    conf = confidence(df, endpoint)
    pca = pca_confidence(df, endpoint)
    writeData(df,supp,conf,pca)

if __name__ == '__main__':
    read()