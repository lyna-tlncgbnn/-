from sklearn.metrics import roc_auc_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc, precision_recall_curve
import numpy as np
import matplotlib.pyplot as plt

# print precision-recall curve
def calculate_PR(labels, preds, pred_val):
    if type(labels) is not np.ndarray:
        preds = preds.detach().cpu().numpy()
        preds_val_np = pred_val.detach().cpu().numpy()
        labels = labels.detach().cpu().numpy()
    print('roc_auc_score: ', roc_auc_score(labels, preds))
    cm = confusion_matrix(labels, preds)
    print('confusion_matrix: ')
    print(cm)
    precision = precision_score(labels, preds)
    print('precision: ', precision)
    recall = recall_score(labels, preds)
    print('recall: ', recall)
    f1_sc = f1_score(labels, preds)
    print('f1_score: ', f1_sc)

def draw_ROC(labels, preds):
    if type(labels) is not np.ndarray:
        preds = preds.detach().cpu().numpy()
        labels = labels.detach().cpu().numpy()
    fpr, tpr, thresholds = roc_curve(labels, preds, pos_label=1)
    roc_auc = auc(fpr, tpr)  # auc为Roc曲线下的面积
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate')  # 横坐标是fpr
    plt.ylabel('True Positive Rate')  # 纵坐标是tpr
    plt.title('ROC of test examples')
    plt.show()

def draw_PR(labels, preds):
    # Precision-recall curve
    if type(labels) is not np.ndarray:
        preds = preds.detach().cpu().numpy()
        labels = labels.detach().cpu().numpy()
    # preds_np = 1 - preds_np
    # labels_np = 1 - labels_np
    precision, recall, thresholds = precision_recall_curve(labels, preds)
    precision = np.fliplr([precision])[0]
    recall = np.fliplr([recall])[0]
    AUC_prec_rec = np.trapz(precision, recall)
    print("\nArea under Precision-Recall curve: " + str(AUC_prec_rec))
    prec_rec_curve = plt.figure()
    plt.plot(recall, precision, '-', label='Area Under the Curve (AUC = %0.4f)' % AUC_prec_rec)
    plt.title('Precision - Recall curve')
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend(loc="lower right")
    plt.show()
    # plt.savefig(output_folder + "Precision_recall.png")