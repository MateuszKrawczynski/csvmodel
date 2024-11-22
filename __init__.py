try:
    import pandas as pd
except:
    print("CsvModel debugger: CsvModel requires pandas library to be installed")
import importlib
DELIMETER = ";"
params_for_each_result_dict = dict()
class train:
    def save(CSV_PATH: str,MODEL_NAME: str):
        if (CSV_PATH == "") or (CSV_PATH == None):
            print("CsvModel debugger: CSV_PATH not defined")
            exit()
        else:
            csv = pd.read_csv(CSV_PATH,delimiter=DELIMETER)
            RESULTS = csv.iloc[:,0].tolist()
            params_dict = dict()
            params_for_each_result_dict = dict()
            for i in range(csv.shape[1]):

                params_dict[str(i)] = csv.iloc[:,i].tolist()
            for i in range(len(RESULTS)):
                result = RESULTS[i]
                all_params = []
                for y in range(len(params_dict)):
                    this_param = (params_dict[str(y)])[i]
                    all_params.append(str(this_param))
                try:
                    params_for_each_result_dict[result] = all_params
                except:
                    print()
                if (MODEL_NAME == "main") or (MODEL_NAME == "__init__"):
                    print("CsvModel debugger: Model can't have these names: main , __init__")
                    exit()
                else:
                    file = f"params_for_each_result_dict = dict()\nparams_for_each_result_dict = {params_for_each_result_dict}"
                    open(f"{MODEL_NAME}.py","w").write(file)
                    print("CsvModel debugger: Model has been saved")


class load:
    def unload(self=None):
        global params_for_each_result_dict
        params_for_each_result_dict = None
    def help(self=None):
        print("CsvModel debugger: To load your model use the csvmodel.load.model() function and pass to it your model's name")
    def model(MODEL_NAME: str):
        try:
            global params_for_each_result_dict
            MODEL = importlib.import_module(MODEL_NAME)
            params_for_each_result_dict = MODEL.params_for_each_result_dict
        except(Exception):
            print("CsvModel debugger: Loading model failed ")
            print(Exception)
            exit()


def prompt(list_of_parameters):
    if (params_for_each_result_dict == None) or (len(params_for_each_result_dict) == 0):
        print("CsvModel debugger: Model isn't loaded yet")
        exit()
    else:
        params_required = len(params_for_each_result_dict[list(params_for_each_result_dict.keys())[0]]) - 1
        if len(list_of_parameters) == params_required:
            procentages = dict()
            params_ref = []
            results_ref = []
            for i in range(len(params_for_each_result_dict)):
                result = list(params_for_each_result_dict.keys())[i]
                params = params_for_each_result_dict[result]

                params_refactored = []
                for x in range(len(params)):
                    if x == 0:
                        print()
                    else:
                        params_refactored.append(params[x])
                params_ref.append(params_refactored)
                results_ref.append(result)

            for i in range(len(results_ref)):
                matches = 0
                for param_user in list_of_parameters:
                    for element in params_ref[i]:
                        if param_user == element:
                            matches = matches + 1
                            break

                procentages[results_ref[i]] = matches / len(results_ref)
            
            RES = []
            procent = []
            for i in range(len(procentages)):
                key = list(procentages.keys())[i]
                RES.append(key)
                procent.append(procentages[key])
            final_result = RES[(procent.index(max(procent)))]
            return final_result

        else:
            print("CsvModel debugger: You didn't pass correct amount of arguments to the prompt() function")
            exit()









