from flask import Flask, request

app = Flask(__name__)


def flat_list(list_to_flat):
    if not isinstance(list_to_flat, list):
        yield list_to_flat
    else:
        for item in list_to_flat:
            yield from flat_list(item)


@app.route("/", methods=['POST'])
def bubbleSort():
    request_data = request.get_json()
    newSeq = list(flat_list(request_data['arr']))
    newSeq = list(filter(None, newSeq))
    n = len(newSeq)
    print(n)

    if n < 10000:
        for i in range(n - 1):
            flag = 0

            for j in range(n - 1):
                if newSeq[j] > newSeq[j + 1]:
                    tmp = newSeq[j]
                    newSeq[j] = newSeq[j + 1]
                    newSeq[j + 1] = tmp
                    flag = 1
            if flag == 0:
                break

        return(','.join(str(x) for x in newSeq))
    else:
        return("Array is too big")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
